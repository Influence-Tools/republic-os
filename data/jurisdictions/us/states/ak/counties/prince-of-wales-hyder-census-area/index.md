---
type: Jurisdiction
title: "Prince of Wales-Hyder Census Area, AK"
classification: county
fips: "02198"
state: "AK"
demographics:
  population: 5715
  population_under_18: 1345
  population_18_64: 1599
  population_65_plus: 2771
  median_household_income: 61156
  poverty_rate: 12.7
  homeownership_rate: 70.57
  unemployment_rate: 7.65
  median_home_value: 225300
  gini_index: 0.4293
  vacancy_rate: 25.57
  race_white: 2503
  race_black: 14
  race_asian: 123
  race_native: 2107
  hispanic: 220
  bachelors_plus: 818
districts:
  - to: "us/states/ak/districts/00"
    rel: in-district
    area_weight: 0.5685
  - to: "us/states/ak/districts/senate/a"
    rel: in-district
    area_weight: 0.537
  - to: "us/states/ak/districts/house/2"
    rel: in-district
    area_weight: 0.499
  - to: "us/states/ak/districts/house/1"
    rel: in-district
    area_weight: 0.038
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ak]
timestamp: "2026-07-03"
---

# Prince of Wales-Hyder Census Area, AK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5715 |
| Under 18 | 1345 |
| 18–64 | 1599 |
| 65+ | 2771 |
| Median household income | 61156 |
| Poverty rate | 12.7 |
| Homeownership rate | 70.57 |
| Unemployment rate | 7.65 |
| Median home value | 225300 |
| Gini index | 0.4293 |
| Vacancy rate | 25.57 |
| White | 2503 |
| Black | 14 |
| Asian | 123 |
| Native | 2107 |
| Hispanic/Latino | 220 |
| Bachelor's or higher | 818 |

## Districts

- [AK-00](/us/states/ak/districts/00.md) — 57% (congressional)
- [AK Senate District A](/us/states/ak/districts/senate/a.md) — 54% (state senate)
- [AK House District 2](/us/states/ak/districts/house/2.md) — 50% (state house)
- [AK House District 1](/us/states/ak/districts/house/1.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
