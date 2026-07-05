---
type: Jurisdiction
title: "Wayne County, MO"
classification: county
fips: "29223"
state: "MO"
demographics:
  population: 10862
  population_under_18: 2132
  population_18_64: 5999
  population_65_plus: 2731
  median_household_income: 47226
  poverty_rate: 25.72
  homeownership_rate: 75.08
  unemployment_rate: 7.34
  median_home_value: 107400
  gini_index: 0.422
  vacancy_rate: 24.45
  race_white: 10151
  race_black: 46
  race_asian: 30
  race_native: 0
  hispanic: 159
  bachelors_plus: 1396
districts:
  - to: "us/states/mo/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/25"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/153"
    rel: in-district
    area_weight: 0.8368
  - to: "us/states/mo/districts/house/144"
    rel: in-district
    area_weight: 0.163
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Wayne County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10862 |
| Under 18 | 2132 |
| 18–64 | 5999 |
| 65+ | 2731 |
| Median household income | 47226 |
| Poverty rate | 25.72 |
| Homeownership rate | 75.08 |
| Unemployment rate | 7.34 |
| Median home value | 107400 |
| Gini index | 0.422 |
| Vacancy rate | 24.45 |
| White | 10151 |
| Black | 46 |
| Asian | 30 |
| Native | 0 |
| Hispanic/Latino | 159 |
| Bachelor's or higher | 1396 |

## Districts

- [MO-08](/us/states/mo/districts/08.md) — 100% (congressional)
- [MO Senate District 25](/us/states/mo/districts/senate/25.md) — 100% (state senate)
- [MO House District 153](/us/states/mo/districts/house/153.md) — 84% (state house)
- [MO House District 144](/us/states/mo/districts/house/144.md) — 16% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
