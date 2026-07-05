---
type: Jurisdiction
title: "Queen Anne's County, MD"
classification: county
fips: "24035"
state: "MD"
demographics:
  population: 51825
  population_under_18: 10926
  population_18_64: 30179
  population_65_plus: 10720
  median_household_income: 112826
  poverty_rate: 6.44
  homeownership_rate: 82.91
  unemployment_rate: 3.83
  median_home_value: 462700
  gini_index: 0.4274
  vacancy_rate: 9.67
  race_white: 43211
  race_black: 2948
  race_asian: 525
  race_native: 32
  hispanic: 2958
  bachelors_plus: 19849
districts:
  - to: "us/states/md/districts/01"
    rel: in-district
    area_weight: 0.7824
  - to: "us/states/md/districts/senate/36"
    rel: in-district
    area_weight: 0.7725
  - to: "us/states/md/districts/house/36"
    rel: in-district
    area_weight: 0.7725
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, md]
timestamp: "2026-07-03"
---

# Queen Anne's County, MD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 51825 |
| Under 18 | 10926 |
| 18–64 | 30179 |
| 65+ | 10720 |
| Median household income | 112826 |
| Poverty rate | 6.44 |
| Homeownership rate | 82.91 |
| Unemployment rate | 3.83 |
| Median home value | 462700 |
| Gini index | 0.4274 |
| Vacancy rate | 9.67 |
| White | 43211 |
| Black | 2948 |
| Asian | 525 |
| Native | 32 |
| Hispanic/Latino | 2958 |
| Bachelor's or higher | 19849 |

## Districts

- [MD-01](/us/states/md/districts/01.md) — 78% (congressional)
- [MD Senate District 36](/us/states/md/districts/senate/36.md) — 77% (state senate)
- [MD House District 36](/us/states/md/districts/house/36.md) — 77% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
