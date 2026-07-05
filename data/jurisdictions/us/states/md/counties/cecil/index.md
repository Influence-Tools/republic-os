---
type: Jurisdiction
title: "Cecil County, MD"
classification: county
fips: "24015"
state: "MD"
demographics:
  population: 104960
  population_under_18: 23336
  population_18_64: 63699
  population_65_plus: 17925
  median_household_income: 92007
  poverty_rate: 10.85
  homeownership_rate: 75.27
  unemployment_rate: 5.46
  median_home_value: 343400
  gini_index: 0.418
  vacancy_rate: 8.48
  race_white: 85715
  race_black: 7548
  race_asian: 1294
  race_native: 100
  hispanic: 5852
  bachelors_plus: 28718
districts:
  - to: "us/states/md/districts/01"
    rel: in-district
    area_weight: 0.91
  - to: "us/states/md/districts/senate/36"
    rel: in-district
    area_weight: 0.5415
  - to: "us/states/md/districts/senate/35"
    rel: in-district
    area_weight: 0.3595
  - to: "us/states/md/districts/house/36"
    rel: in-district
    area_weight: 0.5415
  - to: "us/states/md/districts/house/35b"
    rel: in-district
    area_weight: 0.3019
  - to: "us/states/md/districts/house/35a"
    rel: in-district
    area_weight: 0.0576
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, md]
timestamp: "2026-07-03"
---

# Cecil County, MD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 104960 |
| Under 18 | 23336 |
| 18–64 | 63699 |
| 65+ | 17925 |
| Median household income | 92007 |
| Poverty rate | 10.85 |
| Homeownership rate | 75.27 |
| Unemployment rate | 5.46 |
| Median home value | 343400 |
| Gini index | 0.418 |
| Vacancy rate | 8.48 |
| White | 85715 |
| Black | 7548 |
| Asian | 1294 |
| Native | 100 |
| Hispanic/Latino | 5852 |
| Bachelor's or higher | 28718 |

## Districts

- [MD-01](/us/states/md/districts/01.md) — 91% (congressional)
- [MD Senate District 36](/us/states/md/districts/senate/36.md) — 54% (state senate)
- [MD Senate District 35](/us/states/md/districts/senate/35.md) — 36% (state senate)
- [MD House District 36](/us/states/md/districts/house/36.md) — 54% (state house)
- [MD House District 35B](/us/states/md/districts/house/35b.md) — 30% (state house)
- [MD House District 35A](/us/states/md/districts/house/35a.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
