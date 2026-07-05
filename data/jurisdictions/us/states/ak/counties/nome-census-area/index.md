---
type: Jurisdiction
title: "Nome Census Area, AK"
classification: county
fips: "02180"
state: "AK"
demographics:
  population: 9866
  population_under_18: 3604
  population_18_64: 3478
  population_65_plus: 2784
  median_household_income: 78681
  poverty_rate: 21.51
  homeownership_rate: 66.83
  unemployment_rate: 16.88
  median_home_value: 211200
  gini_index: 0.439
  vacancy_rate: 31.35
  race_white: 1354
  race_black: 63
  race_asian: 172
  race_native: 7301
  hispanic: 214
  bachelors_plus: 1106
districts:
  - to: "us/states/ak/districts/00"
    rel: in-district
    area_weight: 0.8431
  - to: "us/states/ak/districts/senate/t"
    rel: in-district
    area_weight: 0.8405
  - to: "us/states/ak/districts/house/39"
    rel: in-district
    area_weight: 0.8405
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ak]
timestamp: "2026-07-03"
---

# Nome Census Area, AK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9866 |
| Under 18 | 3604 |
| 18–64 | 3478 |
| 65+ | 2784 |
| Median household income | 78681 |
| Poverty rate | 21.51 |
| Homeownership rate | 66.83 |
| Unemployment rate | 16.88 |
| Median home value | 211200 |
| Gini index | 0.439 |
| Vacancy rate | 31.35 |
| White | 1354 |
| Black | 63 |
| Asian | 172 |
| Native | 7301 |
| Hispanic/Latino | 214 |
| Bachelor's or higher | 1106 |

## Districts

- [AK-00](/us/states/ak/districts/00.md) — 84% (congressional)
- [AK Senate District T](/us/states/ak/districts/senate/t.md) — 84% (state senate)
- [AK House District 39](/us/states/ak/districts/house/39.md) — 84% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
