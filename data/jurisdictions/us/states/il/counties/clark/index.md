---
type: Jurisdiction
title: "Clark County, IL"
classification: county
fips: "17023"
state: "IL"
demographics:
  population: 15266
  population_under_18: 3412
  population_18_64: 8759
  population_65_plus: 3095
  median_household_income: 72927
  poverty_rate: 9.15
  homeownership_rate: 80.29
  unemployment_rate: 3.72
  median_home_value: 132400
  gini_index: 0.4161
  vacancy_rate: 10.29
  race_white: 14540
  race_black: 70
  race_asian: 19
  race_native: 57
  hispanic: 285
  bachelors_plus: 3622
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 0.9969
  - to: "us/states/il/districts/senate/51"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/il/districts/house/102"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Clark County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15266 |
| Under 18 | 3412 |
| 18–64 | 8759 |
| 65+ | 3095 |
| Median household income | 72927 |
| Poverty rate | 9.15 |
| Homeownership rate | 80.29 |
| Unemployment rate | 3.72 |
| Median home value | 132400 |
| Gini index | 0.4161 |
| Vacancy rate | 10.29 |
| White | 14540 |
| Black | 70 |
| Asian | 19 |
| Native | 57 |
| Hispanic/Latino | 285 |
| Bachelor's or higher | 3622 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 100% (congressional)
- [IL Senate District 51](/us/states/il/districts/senate/51.md) — 100% (state senate)
- [IL House District 102](/us/states/il/districts/house/102.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
