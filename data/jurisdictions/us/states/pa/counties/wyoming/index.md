---
type: Jurisdiction
title: "Wyoming County, PA"
classification: county
fips: "42131"
state: "PA"
demographics:
  population: 25967
  population_under_18: 4975
  population_18_64: 15037
  population_65_plus: 5955
  median_household_income: 72460
  poverty_rate: 11.52
  homeownership_rate: 77.91
  unemployment_rate: 4.99
  median_home_value: 215400
  gini_index: 0.4584
  vacancy_rate: 15.38
  race_white: 24372
  race_black: 153
  race_asian: 63
  race_native: 30
  hispanic: 658
  bachelors_plus: 5618
districts:
  - to: "us/states/pa/districts/09"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/pa/districts/senate/20"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/pa/districts/house/110"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Wyoming County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25967 |
| Under 18 | 4975 |
| 18–64 | 15037 |
| 65+ | 5955 |
| Median household income | 72460 |
| Poverty rate | 11.52 |
| Homeownership rate | 77.91 |
| Unemployment rate | 4.99 |
| Median home value | 215400 |
| Gini index | 0.4584 |
| Vacancy rate | 15.38 |
| White | 24372 |
| Black | 153 |
| Asian | 63 |
| Native | 30 |
| Hispanic/Latino | 658 |
| Bachelor's or higher | 5618 |

## Districts

- [PA-09](/us/states/pa/districts/09.md) — 100% (congressional)
- [PA Senate District 20](/us/states/pa/districts/senate/20.md) — 100% (state senate)
- [PA House District 110](/us/states/pa/districts/house/110.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
