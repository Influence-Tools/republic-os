---
type: Jurisdiction
title: "Adams County, OH"
classification: county
fips: "39001"
state: "OH"
demographics:
  population: 27540
  population_under_18: 6569
  population_18_64: 15742
  population_65_plus: 5229
  median_household_income: 50264
  poverty_rate: 20.22
  homeownership_rate: 71.65
  unemployment_rate: 6.45
  median_home_value: 164200
  gini_index: 0.4513
  vacancy_rate: 18.16
  race_white: 26541
  race_black: 110
  race_asian: 132
  race_native: 45
  hispanic: 257
  bachelors_plus: 4115
districts:
  - to: "us/states/oh/districts/02"
    rel: in-district
    area_weight: 0.9989
  - to: "us/states/oh/districts/senate/14"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/oh/districts/house/90"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Adams County, OH

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27540 |
| Under 18 | 6569 |
| 18–64 | 15742 |
| 65+ | 5229 |
| Median household income | 50264 |
| Poverty rate | 20.22 |
| Homeownership rate | 71.65 |
| Unemployment rate | 6.45 |
| Median home value | 164200 |
| Gini index | 0.4513 |
| Vacancy rate | 18.16 |
| White | 26541 |
| Black | 110 |
| Asian | 132 |
| Native | 45 |
| Hispanic/Latino | 257 |
| Bachelor's or higher | 4115 |

## Districts

- [OH-02](/us/states/oh/districts/02.md) — 100% (congressional)
- [OH Senate District 14](/us/states/oh/districts/senate/14.md) — 100% (state senate)
- [OH House District 90](/us/states/oh/districts/house/90.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
