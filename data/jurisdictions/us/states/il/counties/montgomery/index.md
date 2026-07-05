---
type: Jurisdiction
title: "Montgomery County, IL"
classification: county
fips: "17135"
state: "IL"
demographics:
  population: 27942
  population_under_18: 5621
  population_18_64: 16314
  population_65_plus: 6007
  median_household_income: 63620
  poverty_rate: 12.6
  homeownership_rate: 77.37
  unemployment_rate: 4.73
  median_home_value: 112300
  gini_index: 0.4448
  vacancy_rate: 9.41
  race_white: 25911
  race_black: 926
  race_asian: 110
  race_native: 31
  hispanic: 609
  bachelors_plus: 5000
districts:
  - to: "us/states/il/districts/15"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/il/districts/senate/54"
    rel: in-district
    area_weight: 0.8942
  - to: "us/states/il/districts/senate/55"
    rel: in-district
    area_weight: 0.1058
  - to: "us/states/il/districts/house/108"
    rel: in-district
    area_weight: 0.7356
  - to: "us/states/il/districts/house/107"
    rel: in-district
    area_weight: 0.1586
  - to: "us/states/il/districts/house/110"
    rel: in-district
    area_weight: 0.1058
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Montgomery County, IL

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27942 |
| Under 18 | 5621 |
| 18–64 | 16314 |
| 65+ | 6007 |
| Median household income | 63620 |
| Poverty rate | 12.6 |
| Homeownership rate | 77.37 |
| Unemployment rate | 4.73 |
| Median home value | 112300 |
| Gini index | 0.4448 |
| Vacancy rate | 9.41 |
| White | 25911 |
| Black | 926 |
| Asian | 110 |
| Native | 31 |
| Hispanic/Latino | 609 |
| Bachelor's or higher | 5000 |

## Districts

- [IL-15](/us/states/il/districts/15.md) — 100% (congressional)
- [IL Senate District 54](/us/states/il/districts/senate/54.md) — 89% (state senate)
- [IL Senate District 55](/us/states/il/districts/senate/55.md) — 11% (state senate)
- [IL House District 108](/us/states/il/districts/house/108.md) — 74% (state house)
- [IL House District 107](/us/states/il/districts/house/107.md) — 16% (state house)
- [IL House District 110](/us/states/il/districts/house/110.md) — 11% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
