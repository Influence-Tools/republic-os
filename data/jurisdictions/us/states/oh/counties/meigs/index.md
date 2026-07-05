---
type: Jurisdiction
title: "Meigs County, OH"
classification: county
fips: "39105"
state: "OH"
demographics:
  population: 21896
  population_under_18: 4509
  population_18_64: 12748
  population_65_plus: 4639
  median_household_income: 46873
  poverty_rate: 21.79
  homeownership_rate: 75.41
  unemployment_rate: 5.39
  median_home_value: 119300
  gini_index: 0.438
  vacancy_rate: 14.74
  race_white: 21074
  race_black: 199
  race_asian: 56
  race_native: 3
  hispanic: 116
  bachelors_plus: 2507
districts:
  - to: "us/states/oh/districts/02"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/oh/districts/senate/30"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/oh/districts/house/94"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Meigs County, OH

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21896 |
| Under 18 | 4509 |
| 18–64 | 12748 |
| 65+ | 4639 |
| Median household income | 46873 |
| Poverty rate | 21.79 |
| Homeownership rate | 75.41 |
| Unemployment rate | 5.39 |
| Median home value | 119300 |
| Gini index | 0.438 |
| Vacancy rate | 14.74 |
| White | 21074 |
| Black | 199 |
| Asian | 56 |
| Native | 3 |
| Hispanic/Latino | 116 |
| Bachelor's or higher | 2507 |

## Districts

- [OH-02](/us/states/oh/districts/02.md) — 100% (congressional)
- [OH Senate District 30](/us/states/oh/districts/senate/30.md) — 100% (state senate)
- [OH House District 94](/us/states/oh/districts/house/94.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
