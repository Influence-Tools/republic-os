---
type: Jurisdiction
title: "Charles County, MD"
classification: county
fips: "24017"
state: "MD"
demographics:
  population: 170527
  population_under_18: 40722
  population_18_64: 106455
  population_65_plus: 23350
  median_household_income: 122816
  poverty_rate: 6.87
  homeownership_rate: 82.07
  unemployment_rate: 4.85
  median_home_value: 428500
  gini_index: 0.3883
  vacancy_rate: 4.6
  race_white: 56930
  race_black: 83988
  race_asian: 5699
  race_native: 1053
  hispanic: 13500
  bachelors_plus: 55907
districts:
  - to: "us/states/md/districts/05"
    rel: in-district
    area_weight: 0.7551
  - to: "us/states/md/districts/senate/28"
    rel: in-district
    area_weight: 0.6663
  - to: "us/states/md/districts/senate/27"
    rel: in-district
    area_weight: 0.0872
  - to: "us/states/md/districts/house/28"
    rel: in-district
    area_weight: 0.6663
  - to: "us/states/md/districts/house/27a"
    rel: in-district
    area_weight: 0.0871
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, md]
timestamp: "2026-07-03"
---

# Charles County, MD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 170527 |
| Under 18 | 40722 |
| 18–64 | 106455 |
| 65+ | 23350 |
| Median household income | 122816 |
| Poverty rate | 6.87 |
| Homeownership rate | 82.07 |
| Unemployment rate | 4.85 |
| Median home value | 428500 |
| Gini index | 0.3883 |
| Vacancy rate | 4.6 |
| White | 56930 |
| Black | 83988 |
| Asian | 5699 |
| Native | 1053 |
| Hispanic/Latino | 13500 |
| Bachelor's or higher | 55907 |

## Districts

- [MD-05](/us/states/md/districts/05.md) — 76% (congressional)
- [MD Senate District 28](/us/states/md/districts/senate/28.md) — 67% (state senate)
- [MD Senate District 27](/us/states/md/districts/senate/27.md) — 9% (state senate)
- [MD House District 28](/us/states/md/districts/house/28.md) — 67% (state house)
- [MD House District 27A](/us/states/md/districts/house/27a.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
