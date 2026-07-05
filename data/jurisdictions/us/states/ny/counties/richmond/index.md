---
type: Jurisdiction
title: "Richmond County, NY"
classification: county
fips: "36085"
state: "NY"
demographics:
  population: 494956
  population_under_18: 106789
  population_18_64: 302912
  population_65_plus: 85255
  median_household_income: 98333
  poverty_rate: 11.49
  homeownership_rate: 67.74
  unemployment_rate: 5.57
  median_home_value: 675500
  gini_index: 0.4492
  vacancy_rate: 7.5
  race_white: 294959
  race_black: 48641
  race_asian: 63222
  race_native: 2575
  hispanic: 96941
  bachelors_plus: 172990
districts:
  - to: "us/states/ny/districts/11"
    rel: in-district
    area_weight: 0.6033
  - to: "us/states/ny/districts/senate/24"
    rel: in-district
    area_weight: 0.4442
  - to: "us/states/ny/districts/senate/23"
    rel: in-district
    area_weight: 0.117
  - to: "us/states/ny/districts/house/62"
    rel: in-district
    area_weight: 0.1966
  - to: "us/states/ny/districts/house/63"
    rel: in-district
    area_weight: 0.182
  - to: "us/states/ny/districts/house/64"
    rel: in-district
    area_weight: 0.1188
  - to: "us/states/ny/districts/house/61"
    rel: in-district
    area_weight: 0.0638
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Richmond County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 494956 |
| Under 18 | 106789 |
| 18–64 | 302912 |
| 65+ | 85255 |
| Median household income | 98333 |
| Poverty rate | 11.49 |
| Homeownership rate | 67.74 |
| Unemployment rate | 5.57 |
| Median home value | 675500 |
| Gini index | 0.4492 |
| Vacancy rate | 7.5 |
| White | 294959 |
| Black | 48641 |
| Asian | 63222 |
| Native | 2575 |
| Hispanic/Latino | 96941 |
| Bachelor's or higher | 172990 |

## Districts

- [NY-11](/us/states/ny/districts/11.md) — 60% (congressional)
- [NY Senate District 24](/us/states/ny/districts/senate/24.md) — 44% (state senate)
- [NY Senate District 23](/us/states/ny/districts/senate/23.md) — 12% (state senate)
- [NY House District 62](/us/states/ny/districts/house/62.md) — 20% (state house)
- [NY House District 63](/us/states/ny/districts/house/63.md) — 18% (state house)
- [NY House District 64](/us/states/ny/districts/house/64.md) — 12% (state house)
- [NY House District 61](/us/states/ny/districts/house/61.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
