---
type: Jurisdiction
title: "Bureau County, IL"
classification: county
fips: "17011"
state: "IL"
demographics:
  population: 32866
  population_under_18: 6799
  population_18_64: 18453
  population_65_plus: 7614
  median_household_income: 69257
  poverty_rate: 10.76
  homeownership_rate: 76.06
  unemployment_rate: 4.26
  median_home_value: 126900
  gini_index: 0.4216
  vacancy_rate: 10.25
  race_white: 28743
  race_black: 193
  race_asian: 287
  race_native: 11
  hispanic: 3357
  bachelors_plus: 6706
districts:
  - to: "us/states/il/districts/16"
    rel: in-district
    area_weight: 0.8173
  - to: "us/states/il/districts/14"
    rel: in-district
    area_weight: 0.1827
  - to: "us/states/il/districts/senate/37"
    rel: in-district
    area_weight: 0.8782
  - to: "us/states/il/districts/senate/53"
    rel: in-district
    area_weight: 0.0629
  - to: "us/states/il/districts/senate/38"
    rel: in-district
    area_weight: 0.0589
  - to: "us/states/il/districts/house/73"
    rel: in-district
    area_weight: 0.8782
  - to: "us/states/il/districts/house/105"
    rel: in-district
    area_weight: 0.0629
  - to: "us/states/il/districts/house/76"
    rel: in-district
    area_weight: 0.0589
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Bureau County, IL

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 32866 |
| Under 18 | 6799 |
| 18–64 | 18453 |
| 65+ | 7614 |
| Median household income | 69257 |
| Poverty rate | 10.76 |
| Homeownership rate | 76.06 |
| Unemployment rate | 4.26 |
| Median home value | 126900 |
| Gini index | 0.4216 |
| Vacancy rate | 10.25 |
| White | 28743 |
| Black | 193 |
| Asian | 287 |
| Native | 11 |
| Hispanic/Latino | 3357 |
| Bachelor's or higher | 6706 |

## Districts

- [IL-16](/us/states/il/districts/16.md) — 82% (congressional)
- [IL-14](/us/states/il/districts/14.md) — 18% (congressional)
- [IL Senate District 37](/us/states/il/districts/senate/37.md) — 88% (state senate)
- [IL Senate District 53](/us/states/il/districts/senate/53.md) — 6% (state senate)
- [IL Senate District 38](/us/states/il/districts/senate/38.md) — 6% (state senate)
- [IL House District 73](/us/states/il/districts/house/73.md) — 88% (state house)
- [IL House District 105](/us/states/il/districts/house/105.md) — 6% (state house)
- [IL House District 76](/us/states/il/districts/house/76.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
