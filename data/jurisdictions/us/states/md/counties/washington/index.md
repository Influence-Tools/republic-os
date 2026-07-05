---
type: Jurisdiction
title: "Washington County, MD"
classification: county
fips: "24043"
state: "MD"
demographics:
  population: 155709
  population_under_18: 33870
  population_18_64: 93686
  population_65_plus: 28153
  median_household_income: 77747
  poverty_rate: 12.42
  homeownership_rate: 66.76
  unemployment_rate: 4.22
  median_home_value: 296100
  gini_index: 0.4396
  vacancy_rate: 6.75
  race_white: 116696
  race_black: 18030
  race_asian: 2531
  race_native: 331
  hispanic: 12297
  bachelors_plus: 37212
districts:
  - to: "us/states/md/districts/06"
    rel: in-district
    area_weight: 0.9981
  - to: "us/states/md/districts/senate/2"
    rel: in-district
    area_weight: 0.5684
  - to: "us/states/md/districts/senate/1"
    rel: in-district
    area_weight: 0.4303
  - to: "us/states/md/districts/house/2a"
    rel: in-district
    area_weight: 0.5416
  - to: "us/states/md/districts/house/1c"
    rel: in-district
    area_weight: 0.4303
  - to: "us/states/md/districts/house/2b"
    rel: in-district
    area_weight: 0.0268
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, md]
timestamp: "2026-07-03"
---

# Washington County, MD

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 155709 |
| Under 18 | 33870 |
| 18–64 | 93686 |
| 65+ | 28153 |
| Median household income | 77747 |
| Poverty rate | 12.42 |
| Homeownership rate | 66.76 |
| Unemployment rate | 4.22 |
| Median home value | 296100 |
| Gini index | 0.4396 |
| Vacancy rate | 6.75 |
| White | 116696 |
| Black | 18030 |
| Asian | 2531 |
| Native | 331 |
| Hispanic/Latino | 12297 |
| Bachelor's or higher | 37212 |

## Districts

- [MD-06](/us/states/md/districts/06.md) — 100% (congressional)
- [MD Senate District 2](/us/states/md/districts/senate/2.md) — 57% (state senate)
- [MD Senate District 1](/us/states/md/districts/senate/1.md) — 43% (state senate)
- [MD House District 2A](/us/states/md/districts/house/2a.md) — 54% (state house)
- [MD House District 1C](/us/states/md/districts/house/1c.md) — 43% (state house)
- [MD House District 2B](/us/states/md/districts/house/2b.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
