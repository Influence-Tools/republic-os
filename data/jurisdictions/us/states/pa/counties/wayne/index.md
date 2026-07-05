---
type: Jurisdiction
title: "Wayne County, PA"
classification: county
fips: "42127"
state: "PA"
demographics:
  population: 51262
  population_under_18: 8408
  population_18_64: 29747
  population_65_plus: 13107
  median_household_income: 62381
  poverty_rate: 12.12
  homeownership_rate: 80.52
  unemployment_rate: 6.01
  median_home_value: 242100
  gini_index: 0.4486
  vacancy_rate: 35.11
  race_white: 45605
  race_black: 1657
  race_asian: 389
  race_native: 88
  hispanic: 2638
  bachelors_plus: 13213
districts:
  - to: "us/states/pa/districts/08"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/pa/districts/senate/20"
    rel: in-district
    area_weight: 0.7224
  - to: "us/states/pa/districts/senate/40"
    rel: in-district
    area_weight: 0.2771
  - to: "us/states/pa/districts/house/111"
    rel: in-district
    area_weight: 0.7117
  - to: "us/states/pa/districts/house/139"
    rel: in-district
    area_weight: 0.2878
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Wayne County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 51262 |
| Under 18 | 8408 |
| 18–64 | 29747 |
| 65+ | 13107 |
| Median household income | 62381 |
| Poverty rate | 12.12 |
| Homeownership rate | 80.52 |
| Unemployment rate | 6.01 |
| Median home value | 242100 |
| Gini index | 0.4486 |
| Vacancy rate | 35.11 |
| White | 45605 |
| Black | 1657 |
| Asian | 389 |
| Native | 88 |
| Hispanic/Latino | 2638 |
| Bachelor's or higher | 13213 |

## Districts

- [PA-08](/us/states/pa/districts/08.md) — 100% (congressional)
- [PA Senate District 20](/us/states/pa/districts/senate/20.md) — 72% (state senate)
- [PA Senate District 40](/us/states/pa/districts/senate/40.md) — 28% (state senate)
- [PA House District 111](/us/states/pa/districts/house/111.md) — 71% (state house)
- [PA House District 139](/us/states/pa/districts/house/139.md) — 29% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
