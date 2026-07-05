---
type: Jurisdiction
title: "Clay County, IN"
classification: county
fips: "18021"
state: "IN"
demographics:
  population: 26409
  population_under_18: 6053
  population_18_64: 15370
  population_65_plus: 4986
  median_household_income: 70010
  poverty_rate: 11.71
  homeownership_rate: 80.86
  unemployment_rate: 3.23
  median_home_value: 153000
  gini_index: 0.496
  vacancy_rate: 9.41
  race_white: 24987
  race_black: 139
  race_asian: 114
  race_native: 5
  hispanic: 523
  bachelors_plus: 4929
districts:
  - to: "us/states/in/districts/08"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/senate/38"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/in/districts/house/46"
    rel: in-district
    area_weight: 0.6
  - to: "us/states/in/districts/house/42"
    rel: in-district
    area_weight: 0.3999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Clay County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26409 |
| Under 18 | 6053 |
| 18–64 | 15370 |
| 65+ | 4986 |
| Median household income | 70010 |
| Poverty rate | 11.71 |
| Homeownership rate | 80.86 |
| Unemployment rate | 3.23 |
| Median home value | 153000 |
| Gini index | 0.496 |
| Vacancy rate | 9.41 |
| White | 24987 |
| Black | 139 |
| Asian | 114 |
| Native | 5 |
| Hispanic/Latino | 523 |
| Bachelor's or higher | 4929 |

## Districts

- [IN-08](/us/states/in/districts/08.md) — 100% (congressional)
- [IN Senate District 38](/us/states/in/districts/senate/38.md) — 100% (state senate)
- [IN House District 46](/us/states/in/districts/house/46.md) — 60% (state house)
- [IN House District 42](/us/states/in/districts/house/42.md) — 40% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
