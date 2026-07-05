---
type: Jurisdiction
title: "Frederick County, MD"
classification: county
fips: "24021"
state: "MD"
demographics:
  population: 287048
  population_under_18: 66996
  population_18_64: 176170
  population_65_plus: 43882
  median_household_income: 122002
  poverty_rate: 6.0
  homeownership_rate: 77.02
  unemployment_rate: 3.31
  median_home_value: 464600
  gini_index: 0.3983
  vacancy_rate: 3.94
  race_white: 193768
  race_black: 30128
  race_asian: 17011
  race_native: 938
  hispanic: 36962
  bachelors_plus: 130282
districts:
  - to: "us/states/md/districts/06"
    rel: in-district
    area_weight: 0.997
  - to: "us/states/md/districts/senate/4"
    rel: in-district
    area_weight: 0.7841
  - to: "us/states/md/districts/senate/2"
    rel: in-district
    area_weight: 0.1168
  - to: "us/states/md/districts/senate/3"
    rel: in-district
    area_weight: 0.0967
  - to: "us/states/md/districts/house/4"
    rel: in-district
    area_weight: 0.7841
  - to: "us/states/md/districts/house/2a"
    rel: in-district
    area_weight: 0.1168
  - to: "us/states/md/districts/house/3"
    rel: in-district
    area_weight: 0.0967
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, md]
timestamp: "2026-07-03"
---

# Frederick County, MD

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 287048 |
| Under 18 | 66996 |
| 18–64 | 176170 |
| 65+ | 43882 |
| Median household income | 122002 |
| Poverty rate | 6.0 |
| Homeownership rate | 77.02 |
| Unemployment rate | 3.31 |
| Median home value | 464600 |
| Gini index | 0.3983 |
| Vacancy rate | 3.94 |
| White | 193768 |
| Black | 30128 |
| Asian | 17011 |
| Native | 938 |
| Hispanic/Latino | 36962 |
| Bachelor's or higher | 130282 |

## Districts

- [MD-06](/us/states/md/districts/06.md) — 100% (congressional)
- [MD Senate District 4](/us/states/md/districts/senate/4.md) — 78% (state senate)
- [MD Senate District 2](/us/states/md/districts/senate/2.md) — 12% (state senate)
- [MD Senate District 3](/us/states/md/districts/senate/3.md) — 10% (state senate)
- [MD House District 4](/us/states/md/districts/house/4.md) — 78% (state house)
- [MD House District 2A](/us/states/md/districts/house/2a.md) — 12% (state house)
- [MD House District 3](/us/states/md/districts/house/3.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
