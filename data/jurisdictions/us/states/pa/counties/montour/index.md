---
type: Jurisdiction
title: "Montour County, PA"
classification: county
fips: "42093"
state: "PA"
demographics:
  population: 18103
  population_under_18: 3642
  population_18_64: 10520
  population_65_plus: 3941
  median_household_income: 76976
  poverty_rate: 8.84
  homeownership_rate: 68.49
  unemployment_rate: 2.92
  median_home_value: 248100
  gini_index: 0.4894
  vacancy_rate: 3.46
  race_white: 16230
  race_black: 439
  race_asian: 622
  race_native: 15
  hispanic: 564
  bachelors_plus: 7947
districts:
  - to: "us/states/pa/districts/09"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/pa/districts/senate/27"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/pa/districts/house/108"
    rel: in-district
    area_weight: 0.9992
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Montour County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18103 |
| Under 18 | 3642 |
| 18–64 | 10520 |
| 65+ | 3941 |
| Median household income | 76976 |
| Poverty rate | 8.84 |
| Homeownership rate | 68.49 |
| Unemployment rate | 2.92 |
| Median home value | 248100 |
| Gini index | 0.4894 |
| Vacancy rate | 3.46 |
| White | 16230 |
| Black | 439 |
| Asian | 622 |
| Native | 15 |
| Hispanic/Latino | 564 |
| Bachelor's or higher | 7947 |

## Districts

- [PA-09](/us/states/pa/districts/09.md) — 100% (congressional)
- [PA Senate District 27](/us/states/pa/districts/senate/27.md) — 100% (state senate)
- [PA House District 108](/us/states/pa/districts/house/108.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
