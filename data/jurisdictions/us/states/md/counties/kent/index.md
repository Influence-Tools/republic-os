---
type: Jurisdiction
title: "Kent County, MD"
classification: county
fips: "24029"
state: "MD"
demographics:
  population: 19346
  population_under_18: 2989
  population_18_64: 11052
  population_65_plus: 5305
  median_household_income: 80147
  poverty_rate: 9.66
  homeownership_rate: 72.54
  unemployment_rate: 2.95
  median_home_value: 330900
  gini_index: 0.4527
  vacancy_rate: 18.04
  race_white: 14903
  race_black: 2707
  race_asian: 242
  race_native: 2
  hispanic: 1126
  bachelors_plus: 8072
districts:
  - to: "us/states/md/districts/01"
    rel: in-district
    area_weight: 0.7294
  - to: "us/states/md/districts/senate/36"
    rel: in-district
    area_weight: 0.7245
  - to: "us/states/md/districts/house/36"
    rel: in-district
    area_weight: 0.7245
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, md]
timestamp: "2026-07-03"
---

# Kent County, MD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19346 |
| Under 18 | 2989 |
| 18–64 | 11052 |
| 65+ | 5305 |
| Median household income | 80147 |
| Poverty rate | 9.66 |
| Homeownership rate | 72.54 |
| Unemployment rate | 2.95 |
| Median home value | 330900 |
| Gini index | 0.4527 |
| Vacancy rate | 18.04 |
| White | 14903 |
| Black | 2707 |
| Asian | 242 |
| Native | 2 |
| Hispanic/Latino | 1126 |
| Bachelor's or higher | 8072 |

## Districts

- [MD-01](/us/states/md/districts/01.md) — 73% (congressional)
- [MD Senate District 36](/us/states/md/districts/senate/36.md) — 72% (state senate)
- [MD House District 36](/us/states/md/districts/house/36.md) — 72% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
